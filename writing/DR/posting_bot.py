# Script responsibility will be to automate posting content to my website
# It will work with an input file (text_to_post)
# The output files (or the files to be written) will be (index_page) and the post_file
# The text to emanate only from the script will be the date
# The text to be used from the input files will be a blob of html to post (input 1) and the number for the last update (input file 2).
# The script will extract the heading from the blob of html content and the last update's number which will be incremented by one for the next update.
# the script will after updating the output files send system commands to
# effectuate a git commit and a git push
# the script will ensure the last update has it's next_post button updated also
# the script will then update the input file's last update key to be the number 
# for the post last posted.
# the text will have hardcoded within it a template in the format of a 
# formattable string where the changing fields will be the text content, the 
# update title, update number, link to previous post and link to next post


# needed
# way to store input text (.txt)
# way to extract html from an html string (regex)
# way to 
from datetime import date
import os

# HTML template
new_post_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
.next-buttons {0}
</style>
<title>Daily Reflections</title>
</head>
<body>
<header>
{1}
</header>
<hr>
<div class="date">
E{2}|{3}
</div>
<hr>
<div class="content">
<div class="audio-recording">
    <audio controls>
        <source src="{4}" type="audio/mp4">
        Your browser does not support the audio element.
    </audio>
</div>
{5}
<div class="next-buttons">
    <button><a href="{6}">previous post</a></button>
</div>
</div>
</body>
</html>
"""

# File names and templates
css = """
 {display: flex;
    justify-content: space-between;
    align-items: center;}
"""

h3_text_file = "h3_text.txt"
previous_episode_no_file = "previous_post_no.txt"
main_content_file = "raw_html.txt"
podcast_file_name_template = "DR_{}.m4a"
previous_post_link_template = "./published_posts/DR_{}/DR_{}.html"
output_folder_name_template = "./published_posts/DR_{}/"
output_html_file_name_template = "DR_{}.html"

# Initialize variables
h3 = ""
previous_episode_number = 0
current_episode_number = ""
post_date = ""
main_content = ""
podcast_file_name = ""
previous_post_link = ""
output_html_file_name = ""
output_folder_name = ""

try:
    # Read h3 text
    if os.path.exists(h3_text_file):
        with open(h3_text_file, 'r') as f:
            h3 = f.read().strip()
    else:
        print(f"Error: {h3_text_file} not found.")
        h3 = "Default Header"

    # Read previous episode number
    if os.path.exists(previous_episode_no_file):
        with open(previous_episode_no_file, 'r') as f:
            previous_episode_number = int(f.read().strip())
    else:
        print(f"Error: {previous_episode_no_file} not found. Using default value 0.")
        previous_episode_number = 0

    # Read main content
    if os.path.exists(main_content_file):
        with open(main_content_file, 'r') as f:
            main_content = f.read().strip()
    else:
        print(f"Error: {main_content_file} not found.")
        main_content = "<p>No content available.</p>"

    # Generate post date in format dd.mm.yy
    post_date = date.today().strftime("%d.%m.%y")
    print(f"Post date: {post_date}")

    # Calculate current episode number
    current_episode_number = previous_episode_number + 1
    current_episode_number = f"{current_episode_number:03d}"  # Ensure 3-digit format (e.g., 001, 012)
    print(f"Current episode number: {current_episode_number}")

    # Generate file names and links
    podcast_file_name = podcast_file_name_template.format(current_episode_number)
    print(f"Podcast file name: {podcast_file_name}")

    output_html_file_name = output_html_file_name_template.format(current_episode_number)
    print(f"Output HTML file name: {output_html_file_name}")

    output_folder_name = output_folder_name_template.format(current_episode_number)
    print(f"Output folder name: {output_folder_name}")
    
    previous_episode_number = f"{previous_episode_number:03d}"  # Ensure 3-digit format (e.g., 001, 012)
    previous_post_link = previous_post_link_template.format(previous_episode_number, previous_episode_number)
    print(f"Previous post link: {previous_post_link}")

    # Format the HTML content
    output_content = new_post_template.format(
        css,
        h3,
        current_episode_number,
        post_date,
        podcast_file_name,
        main_content,
        previous_post_link
    )

    # Print the generated HTML for debugging
    print("\nGenerated HTML:\n")
    print(output_content)

    # Optionally, save the output to a file
    os.makedirs(output_folder_name, exist_ok=True)
    output_path = os.path.join(output_folder_name, output_html_file_name)
    with open(output_path, 'w') as f:
        f.write(output_content)
        
    print(f"\nHTML file saved to: {output_path}")

    # Update the previous episode number file
    with open(previous_episode_no_file, 'w') as f:
        f.write(str(current_episode_number))
    print(f"Updated {previous_episode_no_file} with episode number: {current_episode_number}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    
# commit and push changes to git
os.system("git add .")
os.system(f"git commit -m 'Updated post {current_episode_number}'")
os.system("git push origin main")
