# -*- coding: utf-8 -*-
import os
import sys, io

# تأكد أن الطباعة UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE_DIR = r"D:\FlutterAI\scripts"   # غير المسار إذا لزم
OUTPUT_FILE = os.path.join(BASE_DIR, "all_py_code.txt")

def collect_py_files(base_dir, output_file):
    with open(output_file, "w", encoding="utf-8") as out:
        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    out.write(f"\n\n{'='*80}\n📄 File: {file_path}\n{'='*80}\n\n")
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            out.write(f.read())
                    except Exception as e:
                        out.write(f"\n❌ Error reading {file_path}: {e}\n")

    print(f"\n✅ تم نسخ جميع الأكواد إلى: {output_file}")

if __name__ == "__main__":
    collect_py_files(BASE_DIR, OUTPUT_FILE)
