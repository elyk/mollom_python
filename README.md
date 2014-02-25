# mollom_python

A python client library for the [Mollom REST API](https://mollom.com/api).

## Requirements
* requests\_oauthlib
* requests

These requirements can be installed by doing 
```
pip install -r requirements.txt
```

## Example Usage
```python
from mollom_python import Mollom
public_key = {public_key}
private_key = {private_key}
mollom_client = Mollom(public_key, private_key)

try:
  post_title = {post_title}
  post_body = {post_body}
  author_id = {author_id}
  author_ip = {author_ip}
  content_id, spam_classification = mollom_client.check_content(post_title=post_title, post_body=post_body, author_id=author_id, author_ip=author_ip)
  
  if spam_classification == "ham":
    # Accept the content
  elif spam_classification == "spam":
    # Reject the content
  else: # unsure
    captcha_id, captcha_url = mollom_client.create_captcha(content_id=content_id)
    
    # Present captcha_url to the end-user for a solution
    solution = {solution}
    
    solved = mollom_client.check_captcha(captcha_id=captcha_id, solution=solution, author_id=author_id, author_ip=author_ip)
    if solved:
      # If the content hasn't changed, accept the content
      # otherwise, resubmit for checking: mollom_client.check_content(content_id=content_id, ...)
    else:
      # User failed to solve the CAPTCHA correctly
      # Either give the user more attempts or simply reject the content
    
except (MollomConnectionError):
  # Mollom is down, accept the content for manual moderation
```

## Sending feedback
Sometimes, Mollom makes mistakes. When this happens, send feedback so that Mollom can learn from its mistakes.
```python
from mollom_python import Mollom
public_key = {public_key}
private_key = {private_key}
mollom_client = Mollom(public_key, private_key)

# Content ID of the content to submit feedback about
content_id = {content_id}

mollom_client.send_feedback(content_id=content_id, reason="spam")
```
