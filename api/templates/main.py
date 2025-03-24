
def upload_file(token: str) -> str:
    result = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>File Upload with Drag and Drop</title>
                        <style>
                            body {
                                font-family: Arial, sans-serif;
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                height: 100vh;
                                margin: 0;
                                background-color: #f0f0f0;
                            }
                            .upload-container {
                                background-color: #fff;
                                padding: 20px;
                                border: 2px dashed #ccc;
                                border-radius: 10px;
                                text-align: center;
                                width: 300px;
                            }
                            .upload-container.dragging {
                                border-color: #007bff;
                            }
                            .upload-container h2 {
                                margin-bottom: 10px;
                            }
                            .upload-container p {
                                color: #555;
                            }
                            .file-input {
                                margin-top: 10px;
                            }
                            .submit-button {
                                margin-top: 10px;
                                padding: 10px;
                                background-color: #007bff;
                                color: #fff;
                                border: none;
                                border-radius: 5px;
                                cursor: pointer;
                            }
                            .submit-button:hover {
                                background-color: #0056b3;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="upload-container" id="uploadContainer">
                            <h2>Drag & Drop or Click to Upload</h2>
                            <p>(or click to select a file)</p>
                            <input type="file" class="file-input" id="fileInput" />
                            <button class="submit-button" id="submitButton">Upload</button>
                        </div>

                        <script>
                            const uploadContainer = document.getElementById('uploadContainer');
                            const fileInput = document.getElementById('fileInput');
                            const submitButton = document.getElementById('submitButton');

                            // Handle drag and drop
                            uploadContainer.addEventListener('dragover', (e) => {
                                e.preventDefault();
                                uploadContainer.classList.add('dragging');
                            });

                            uploadContainer.addEventListener('dragleave', () => {
                                uploadContainer.classList.remove('dragging');
                            });

                            uploadContainer.addEventListener('drop', (e) => {
                                e.preventDefault();
                                uploadContainer.classList.remove('dragging');
                                const files = e.dataTransfer.files;
                                if (files.length > 0) {
                                    fileInput.files = files;
                                }
                            });

                            // Handle file input change
                            fileInput.addEventListener('change', () => {
                                if (fileInput.files.length > 0) {
                                    // File selected, you can handle it here
                                }
                            });

                            // Handle form submission
                            submitButton.addEventListener('click', async () => {
                                const file = fileInput.files[0];

                                if (!file) {
                                    alert('Please select a file.');
                                    return;
                                }

                                const formData = new FormData();
                                formData.append('file', file);

                                try {"""
    result += f"""
                const response = await fetch('/upload?token={token}', """
    result += """
                            {
                                            method: 'POST',
                                            body: formData
                                        });

                                        if (response.ok) {
                                            alert('File uploaded successfully!');
                                        } else {
                                            alert('Failed to upload file. Please try again.');
                                        }
                                    } catch (error) {
                                        console.error('Error uploading file:', error);
                                        alert('An error occurred while uploading the file. Please try again.');
                                    }
                                });
                            </script>
                        </body>
                        </html>"""
    return result