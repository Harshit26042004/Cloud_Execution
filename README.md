# S3 Execution


## Requirements

To run this project, you will need to install the required libraries. You can do this by using the provided `requirements.txt`. Execute the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Tesseract Configuration

For Tesseract OCR configuration, use these steps:

1. **Install Tesseract**: Visit the [Tesseract Installation Guide](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
2. **Copy Tesseract Path**: After installation, locate the `tesseract.exe` file and copy its path.
3. **Update `reader.py`**: Open the `reader.py` file and navigate to line 32. Replace the placeholder with the copied path of `tesseract.exe`.

   Example:
   ```python
   tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Update this path
    ```
## Testing with LocalStack

To test the application with LocalStack, perform the following steps:

1. **Start LocalStack**: Ensure that LocalStack is up and running on your machine.
2. **Configure AWS**: Set up your AWS CLI configuration in the command line (cmd).
3. **Run the Execution Script**: Use the following command to execute the script with the path to your JSON file:

If Tika is used we need java installed in our system!

   ```bash
   python Executions path/to/json_file
