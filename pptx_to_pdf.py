import subprocess

def pptx_to_pdf(input_file, output_directory):
    try:
        result = subprocess.run([
            "libreoffice",
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_directory,
            input_file  
        ], capture_output=True, text=True)

        if result.returncode != 0:
            print("Error occurred during conversion:", result.stderr)
        else:
            # Get the name of the converted file
            pdf_file = input_file.split('/')[-1].replace('.pptx', '.pdf')
            print(f"Successfully converted to {output_directory}/{pdf_file}")

    except Exception as e:
        print("An error occurred:", e)

pptx_to_pdf("/home/rafi/VSCODE/Automate_Script/Assignment.pptx", "/home/rafi/Documents")
