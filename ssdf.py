# import pyfiglet and colorama modules
import pyfiglet
from colorama import init, Fore, Style
import requests

# Initialize colorama
init()

# Function to print ASCII art
def print_ascii_art(text):
    result = pyfiglet.figlet_format(text)
    print(result)


# Function for scanning subdomains
def domain_scanner(domain_name, subdomain_list):
    print('----URLs after scanning subdomains----')

    # Loop for getting URLs
    for subdomain in subdomain_list:
        # Making URL by putting subdomain one by one
        url = f"https://{subdomain}.{domain_name}"

        # Using try-except block to avoid program crashes
        try:
            # Sending GET request to the URL
            response = requests.get(url)

            # Check if the link is live
            if response.status_code == 200:
                print(f'[+] {Fore.GREEN}{url} - Live (Status Code: {response.status_code}){Style.RESET_ALL}')
            else:
                print(f'[-] {Fore.RED}{url} - Not Live (Status Code: {response.status_code}){Style.RESET_ALL}')

        except requests.ConnectionError:
            print(f'[-] {Fore.RED}{url} - Connection Error{Style.RESET_ALL}')


# Main function
if __name__ == '__main__':
    # Print ASCII art for the program name
    print_ascii_art("Simple Subdomain Finder")
    print("Made By V1k1ng138")

    # Input the domain name
    dom_name = input("Enter the Domain Name: ")

    # Input the word list filename
    word_list_file = input("Enter the Word List Filename: ")

    # Opening the word list file
    with open(word_list_file, 'r') as file:
        # Reading the file and splitting it into lines
        word_list = file.read().splitlines()

    # Calling the function for scanning the subdomains
    domain_scanner(dom_name, word_list)
