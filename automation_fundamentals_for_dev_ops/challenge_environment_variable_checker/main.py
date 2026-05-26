def check_env_vars(required_vars, env_vars):
    # Write your code here
    for x in required_vars:
        if x in env_vars:
            print(f"{x.lower()} is set")
        else:
            print(f"{x.lower()} is missing")

    
    

required = ["DB_HOST", "DB_USER", "DB_PASS", "API_KEY"]
env = {"DB_HOST": "localhost", "DB_USER": "admin", "API_KEY": "abcdef"}

check_env_vars(required, env)
