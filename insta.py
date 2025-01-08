import instaloader
import pandas as pd

loader = instaloader.Instaloader()
profile_username = "beerbiceps"


# Load the profile
profile = instaloader.Profile.from_username(loader.context, profile_username)

# Initialize a list to store post data
data = []

# Set the post limit
post_limit = 291
counter = 0

# Set the batch size for saving
batch_size = 50

for post in profile.get_posts():
    if counter >= post_limit:
        break  # Exit the loop after reaching the post limit
    
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
        "Creator": profile_username
    }
    data.append(post_data)
    counter += 1  # Increment the counter
    print(post_data)  # For live feedback

    # Save to CSV after every batch of 50 posts
    if counter % batch_size == 0 or counter == post_limit:
        partial_output_file = f"{profile_username}_instagram_data_batch_{counter // batch_size}.csv"
        df = pd.DataFrame(data)
        df.to_csv(partial_output_file, index=False)
        print(f"Batch saved to {partial_output_file}")
        data = []  # Clear the data list for the next batch

# Save any remaining posts if the last batch was not a full 50 posts
if data:
    final_output_file = f"{profile_username}_instagram_data_batch_{(counter // batch_size) + 1}.csv"
    df = pd.DataFrame(data)
    df.to_csv(final_output_file, index=False)
    print(f"Final batch saved to {final_output_file}")
