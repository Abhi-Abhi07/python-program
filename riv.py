import zipfile
from androguard.misc import AnalyzeAPK

def detect_proguard_signatures(apk_path):
    try:
        # Open the APK as a zip file
        with zipfile.ZipFile(apk_path, 'r') as apk:
            # Check META-INF for ProGuard hints
            meta_inf_files = [f for f in apk.namelist() if f.startswith("META-INF/")]
            if any("proguard" in f.lower() for f in meta_inf_files):
                print("ProGuard-related metadata found in META-INF.")
                return True

        # Analyze classes.dex for obfuscation patterns
        print("Analyzing classes.dex for obfuscation patterns...")
        a, d, dx = AnalyzeAPK(apk_path)
        obfuscated_count = 0

        for class_name in d[0].get_classes():
            class_name_str = class_name.get_name()

            # Check for short or nonsensical class names
            if len(class_name_str) <= 2 or (
                class_name_str.startswith('L') and '$' not in class_name_str and '/' not in class_name_str
            ):
                obfuscated_count += 1

        if obfuscated_count > 0:
            print(f"Detected {obfuscated_count} obfuscated classes. APK likely obfuscated.")
            return True

        print("No clear ProGuard signatures detected.")
        return False

    except Exception as e:
        print(f"Error while analyzing APK: {e}")
        return False

# Replace 'path_to_apk.apk' with your APK file path
apk_file_path =  'C:/Users/gurja/OneDrive/Desktop/apkFile/aeroGCS green.apk'
if detect_proguard_signatures(apk_file_path):
    print("The APK shows signs of ProGuard obfuscation.")
else:
    print("The APK does not show signs of ProGuard obfuscation.")
