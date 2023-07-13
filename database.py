import flet as ft
import json

def main(page: ft.Page):
    
    page.scroll = True
            
    def load_posts_from_json():
        posts = []
        with open('posts.json', 'r') as file:
            for line in file:
                post = json.loads(line)
                posts.append(post) 
                username = post['author']
                title = post['title']
                content = post['content']  
                likes = post['likes']     
                image = post['image_url']
                card = ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.Image(src=image)),
                                    title=ft.Text(title),
                                    subtitle=ft.Text(
                                        content,
                                    ),
                                ),
                                ft.Row(
                                    [ft.TextButton(username), ft.TextButton(likes)],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        ),
                        width=400,
                        padding=10,
                    )
                )
                page.add(card)
                
        return posts
    
    load_posts_from_json()

ft.app(target=main)