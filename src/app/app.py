import subprocess

def handler(event, context): 
    version = subprocess.run(
        ['krb5-config', '--version'],
        capture_output=True
    )
    return 'Hello from Lambda! I am using ' + version.stdout.decode('utf-8').strip('\n') + '!'