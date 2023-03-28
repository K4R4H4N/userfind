import requests

url = "https://www.instagram.com/"

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

for i in alphabet:

    for j in alphabet:

        for k in alphabet:

            for l in alphabet:

                username = i + j + k + l

                response = requests.get(url + username)

                if response.status_code == 404:

                    print(username + " is available!")

