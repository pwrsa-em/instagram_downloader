import instaloader

loader = instaloader.Instaloader()



username = input("username: ")
password = input("password: ")
loader.login(username, password)

link = input("link: ")

post_id = link.split("/")[-2]

def download_file():
    try:
        post = instaloader.Post.from_shortcode(loader.context, post_id)
        loader.download_post(post, target=f"{post.owner_username}_{post_id}")
        print(f"post Downloading successful!")

    except Exception as e:
        print(f"Error: {e}")

def main():
    download_file()

if __name__ == "__main__":
    main()