CUR_DATE = $(shell date +'%Y-%m-%d')
POST_NAME = new-post

new_post:
	cp ./_utils/blog_template.md "_posts/$(CUR_DATE)-$(POST_NAME).md"