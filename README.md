# NextGen OS - Face Authentication System

## Overview
ProjectOS is a **next-gen authentication system** that enables **face recognition-based authentication** for operating systems. It enhances security and convenience by allowing users to log in using their facial biometrics instead of traditional passwords.

## Features
- **Add New Face**: Register a new face for authentication.
- **Match Face**: Authenticate users by matching their face.
- **List Registered Faces**: Display all stored face encodings.
- **Remove Face**: Delete a registered face from the system.
- **Disable Face Recognition**: Temporarily disable face authentication.
- **Configuration**: Manage system settings and preferences.
- **CLI Support**: Command-line interface for easy usage.

## Files and Their Functions
- `add_new_face.py` - Script to add a new user face for authentication.
- `match_face.py` - Matches the detected face with stored face encodings.
- `list_of_faces.py` - Lists all stored face encodings.
- `remove_face.py` - Deletes a registered face from the system.
- `disable_facerecognition.py` - Temporarily disables face authentication.
- `configuration.py` - Manages system configuration settings.
- `cli.py` - Command-line interface for interacting with the system.
- `test_face.py` - Test script to verify face authentication functionality.

## Installation
```bash
# Clone the repository
git clone https://github.com/your-repo/ProjectOS.git
cd ProjectOS

# Install dependencies
pip install -r requirements.txt

# Run face registration
python add_new_face.py
```

## Usage
### Add a new face
```bash
python add_new_face.py
```
### Authenticate a user
```bash
python match_face.py
```
### List all registered faces
```bash
python list_of_faces.py
```
### Remove a face
```bash
python remove_face.py
```
### Disable face recognition
```bash
python disable_facerecognition.py
```

## Dependencies
- OpenCV
- Dlib
- Face Recognition
- NumPy
- Python 3.x

## Future Scope
- **Voice Authentication** Integration
- **Multi-User Face Recognition**
- **AI-Based Spoof Detection** to prevent face spoofing

## Contributing
Feel free to submit issues and pull requests to improve the system.

