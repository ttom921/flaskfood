
# 檢查是否在執行
import subprocess


def checkIfRunning(filename, pid):
    """Check whether the file is running.

        Args:
            filename (str): The filename to be checked.

        Returns:
            Bool: The return value, True for running, False for not running.
    """
    cmd = f"ps -ef | grep {filename} | grep python | grep -v {pid} | wc -l"
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    return True if int(output) > 1 else False
