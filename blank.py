import os

def create_blank_eeproms():
    # Sizes in kilobytes
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    
    # Create directory if it doesn't exist
    output_dir = "blank_eeproms"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate blank files for each size
    for size in sizes:
        # Calculate size in bytes
        bytes_size = size * 1024
        
        # Create filename with proper formatting
        filename = f"{output_dir}/{size:03d}k_blank.bin"
        
        # Create and write blank file filled with 0xFF
        with open(filename, 'wb') as f:
            blank_data = bytes([0xFF] * bytes_size)
            f.write(blank_data)
            
        print(f"Created {filename} ({bytes_size:,} bytes)")

if __name__ == "__main__":
    create_blank_eeproms()