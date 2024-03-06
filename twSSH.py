import paramiko

ssh = paramiko.SSHClient()

def main(exec: str) -> str:
    print(" [DEBUG-SSH] " + exec.lower())
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(exec.lower())
    return(str(ssh_stdout.read().decode() + ssh_stderr.read().decode()))

def init(host: str, user: str, password: str) -> None:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=password)

def exit() -> None:
    ssh.close()
