import instaloader
import pandas as pd


loader = instaloader.Instaloader()
# profile = instaloader.Profile.from_username(L.context, "sakshamchoudharyofficial")
profile_username = "sakshamchoudharyofficial"

profile = instaloader.Profile.from_username(loader.context, profile_username)


# Initialize a list to store post data
data = []

for post in profile.get_posts():
    # Determine post type using typename
    if post.typename == "GraphImage":
        post_type = "Photo"
    elif post.typename == "GraphVideo":
        post_type = "Reel" if post.is_video else "Video"
    elif post.typename == "GraphSidecar":
        post_type = "Carousel"
    else:
        post_type = "Unknown"

    # Extract required details
    post_data = {
        "Caption": post.caption,
        "Likes": post.likes,
        "Views": post.video_view_count if post.is_video else None,
        "Comments": post.comments,
        "Shares": post.video_view_count,  # Proxy for shares
        "Post Type": post_type,
        "Creator": profile_username, 
    }
    data.append(post_data)
    print(post_data)  # For live feedback

# Save the data to a CSV file
output_file = f"{profile_username}_instagram_data.csv"
df = pd.DataFrame(data)
df.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")