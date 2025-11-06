import requests

# Test 1: Valid code
print("Test 1: Valid code")
r = requests.post('http://localhost:5000/generate-docs', json={'code': 'def hello(): print("Hello, world!")'})
print('Status:', r.status_code)
print('Response:', r.text)
print()

# Test 2: Empty code
print("Test 2: Empty code")
r = requests.post('http://localhost:5000/generate-docs', json={'code': ''})
print('Status:', r.status_code)
print('Response:', r.text)
print()

# Test 3: Invalid JSON (missing code key)
print("Test 3: Invalid JSON")
r = requests.post('http://localhost:5000/generate-docs', json={})
print('Status:', r.status_code)
print('Response:', r.text)
print()

# Test 4: Long code
print("Test 4: Long code")
long_code = '''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
for i in range(10):
    print(fibonacci(i))
'''
r = requests.post('http://localhost:5000/generate-docs', json={'code': long_code})
print('Status:', r.status_code)
print('Response:', r.text)
print()
