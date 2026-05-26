def extract_errors(log_entries):
    # Write your code here
    error_lines = []
    # Add logic to populate error_lines with entries containing 'ERROR'
    for x in log_entries:
        if "ERROR" in x:
            error_lines.append(x)
        
    for line in error_lines:
        print(line)
    error_count = len(error_lines)
    print(error_count)

logs = [
    "2024-06-01 12:00:00 INFO Starting backup process",
    "2024-06-01 12:00:01 ERROR Failed to connect to database",
    "2024-06-01 12:00:02 INFO Backup in progress",
    "2024-06-01 12:00:03 ERROR Disk space low",
    "2024-06-01 12:00:04 WARNING Backup delayed",
    "2024-06-01 12:00:05 INFO Backup complete"
]

extract_errors(logs)
