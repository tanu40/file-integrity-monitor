# 🛡️ File Integrity Monitor (FIM) using Python

## 📌 Overview

This project implements a **File Integrity Monitoring (FIM)** system that detects unauthorized changes in files by using **cryptographic hashing (SHA-256)**. It creates a baseline of file hashes and compares them over time to identify modifications, deletions, or newly added files.

---

## 🎯 Objectives

* Monitor file system changes in a target directory
* Detect file tampering or unauthorized modifications
* Identify deleted and newly added files
* Provide a lightweight security monitoring solution

---

## 🚀 Features

* 📂 Recursive directory monitoring
* 🔐 SHA-256 hash-based integrity checking
* 📝 Baseline creation and storage (JSON format)
* 🔍 Detection of:

  * Modified files
  * Deleted files
  * Newly added files
* ⚡ Simple CLI-based interface
* 📸 Output visualization via screenshots

---

## 🛠️ Tech Stack

* Python
* hashlib (SHA-256 hashing)
* os (file traversal)
* json (baseline storage)

---

## 📂 Project Structure

```id="n0h6m9"
file-integrity-monitor/
│── target_folder/        # Files to monitor
│── baseline/
│   └── baseline.json     # Stored file hashes
│── src/
│   └── fim.py            # Main script
│── images/               # Output screenshots
│── README.md
```

---

## ▶️ How to Run

### 1️⃣ Navigate to project directory

```bash id="lx8m2z"
cd file-integrity-monitor/src
```

### 2️⃣ Run the script

```bash id="gm3r7k"
python fim.py
```

> If `python` doesn’t work:

```bash id="yfqk1r"
py fim.py
```

---

## ⚙️ Usage

### 🔹 Create Baseline

* Run the script
* Enter:

```plaintext id="d3gq2f"
1
```

👉 Stores hashes of all files in `baseline.json`

---

### 🔹 Check Integrity

* Run the script again
* Enter:

```plaintext id="v7a4u6"
2
```

---

## 📊 Sample Output

```id="4q7p0v"
[MODIFIED] ../target_folder/file1.txt
[DELETED] ../target_folder/file2.txt
[NEW FILE] ../target_folder/newfile.txt
```

---

## 📸 Output Screenshot

![FIM Output](images/output.png)

---

## 🧠 How It Works

1. Generates SHA-256 hash for each file
2. Stores hashes as baseline
3. Recomputes hashes during integrity check
4. Compares baseline with current state
5. Flags any discrepancies

---

## 🔍 Use Case

This project simulates a **real-world cybersecurity scenario** where:

* File tampering needs to be detected
* System integrity must be maintained
* Unauthorized changes are monitored


## 👤 Author

**Tanushka**

---

## ⭐ Acknowledgment

This project is part of a cybersecurity learning initiative focused on defensive security and system monitoring.
