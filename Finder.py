import re

# Open the ACL Antology file for reading
with open('anthology_abstracts.bib', 'r') as file:
    data = file.read()

# Find all the titles related to your research topic eg: "suicid"
matches = re.findall(r'title\s*=\s*"(.*?)"[\s\S]*?abstract\s*=\s*"(.*?)"', data, re.IGNORECASE)
titles = [title for title, abstract in matches if re.search(r'suicid', title, re.IGNORECASE) or re.search(r'suicid', abstract, re.IGNORECASE)]

# The list all the matching titles to your new title Files
with open('RelatedTopicPapers.txt', 'w') as file:
    for title in titles:
        file.write(title + '\n')
