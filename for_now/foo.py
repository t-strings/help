from some_library import html


@html
def render_user(user: User) -> Template:
	return f"""
	<div>
		<h1>{user.name}</h1>
		<p>{user.email}</p>
	</div>
	"""

type(render_user(user))  # HTMLElement

