import socket
import subprocess
import platform
import sys

def ping_host(host, timeout=2):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', '-w', str(timeout * 1000), host] if platform.system().lower() == 'windows' else ['ping', param, '1', '-W', str(timeout), host]
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout + 5)
        return result.returncode == 0
    except Exception:
        return False

def tcp_connect_test(host, port, timeout=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
        return result == 0
    finally:
        sock.close()

def check_local_firewall_rules(port):
    # Вызываем PowerShell для получения правил фаервола
    ps_cmd = f"""
Get-NetFirewallRule -Direction Inbound -Enabled True -Action Allow |
  Get-NetFirewallPortFilter |
  Where-Object {{ $_.LocalPort -contains {port} -or ($_.LocalPort | ForEach-Object {{ $_ -eq "{port}" }}) }} |
  Select-Object InstanceId | ConvertTo-Json
"""
    try:
        res = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_cmd],
            capture_output=True, text=True, timeout=10
        )
        if res.returncode == 0 and res.stdout.strip():
            return True, res.stdout
        return False, ""
    except Exception as e:
        return False, str(e)

def check_listening_ports(port):
    # netstat: ищем LISTENING на нужном порту
    cmd = ["netstat", "-an"]
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=10).stdout
        lines = [l.strip() for l in out.splitlines()]
        for line in lines:
            if f":{port}" in line and "LISTEN" in line.upper():
                return True
        return False
    except Exception:
        return False

def main():
    host = "45.138.200.171"
    port = 27021

    print(f"Проверка хоста: {host}, порт: {port}")
    print("-" * 60)

    ping_ok = ping_host(host)
    print(f"[Ping] {'OK' if ping_ok else 'FAIL'}")

    tcp_ok = tcp_connect_test(host, port)
    print(f"[TCP:{port}] {'OK' if tcp_ok else 'FAIL'}")

    fw_ok, fw_data = check_local_firewall_rules(port)
    print(f"[Firewall Inbound] {'Есть правило ALLOW на порт' if fw_ok else 'Нет явного правила ALLOW'}")
    if fw_data:
        print(f"Детали правил:\n{fw_data}")

    local_listen = check_listening_ports(port)
    print(f"[Local LISTEN] {'Порт слушает (LISTENING)' if local_listen else 'Не слушает локально'}")

    print("-" * 60)
    if not tcp_ok:
        print("Вывод: TCP‑соединение не удалось. Возможные причины:")
        print("- Сервер выключен или недоступен по сети.")
        print("- Порт не слушает сервис (проверьте netstat на сервере).")
        print("- Блокировка на фаерволе сервера, в Security Groups облака, или на промежуточном оборудовании.")
        print("- ICMP (ping) может быть заблокирован, это не обязательно влияет на TCP.")
    else:
        print("Вывод: TCP‑соединение успешно.")

if __name__ == "__main__":
    # Для работы с фаерволом лучше запускать от администратора
    if platform.system().lower() == "windows":
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("Рекомендуется запустить скрипт от имени администратора (особенно для проверки правил фаервола).")
    main()
