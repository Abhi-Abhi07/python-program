import subprocess
import re

def detect_obfuscation(apk_path):
    """
    Detect obfuscation in an APK file using APKiD and determine the tool used.

    Args:
        apk_path (str): Path to the APK file.

    Returns:
        dict: A dictionary with obfuscation detection results.
    """
    try:
        # Run the APKiD command on the given APK path
        result = subprocess.run(
            ["apkid", apk_path],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            raise Exception(f"APKiD error: {result.stderr}")

        # Parse APKiD output
        output = result.stdout
        print("APKiD Output:\n", output)

        # Check for ProGuard or R8 markers
        obfuscation_detected = False
        tool_used = None

        if "ProGuard" in output:
            obfuscation_detected = True
            tool_used = "ProGuard"
        elif "r8" in output:
            obfuscation_detected = True
            tool_used = "R8"

        # Check for anti-debugging and anti-VM techniques
        anti_debug = "anti_debug" in output
        anti_vm = "anti_vm" in output

        # Return detection results
        return {
            "obfuscation_detected": obfuscation_detected,
            "tool_used": tool_used,
            "anti_debug": anti_debug,
            "anti_vm": anti_vm,
            "raw_output": output
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "obfuscation_detected": False,
            "tool_used": None,
            "anti_debug": False,
            "anti_vm": False,
            "error": str(e)
        }

# Example usage
apk_file_path = r"C:\Users\gurja\OneDrive\Desktop\APKFiles\dronecast.apk"
result = detect_obfuscation(apk_file_path)

print("\nDetection Results:")
print(f"Obfuscation Detected: {result['obfuscation_detected']}")
print(f"Tool Used: {result['tool_used']}")
print(f"Anti-Debugging: {result['anti_debug']}")
print(f"Anti-VM: {result['anti_vm']}")
