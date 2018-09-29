import subprocess


if __name__ == '__main__':
    subprocess.Popen(['pip', 'install', '-r', 'requirements.txt']).wait()
    subprocess.Popen(['python', 'manage.py', 'makemigrations']).wait()
    subprocess.Popen(['python', 'manage.py', 'migrate']).wait()
    subprocess.Popen(['python', 'manage.py', 'runserver']).wait()
