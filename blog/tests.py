from django.test import TestCase, Client
from bs4 import BeautifulSoup
from . models import Post


class TestView(TestCase):
    def setup(self):
        self.client = Client()

    def test_post_list(self):
        #1.1 포스트 목록 페이지를 가져온다.
        response = self.client.get('/blog/') #clinent는 가상의 테스트 유저이다. 127.0.0.1 8000/blog/ 들어갈시에 나오는 페이지의 정보를 response 함수에 담는다.

        #1.2 정상적으로 페이지가 로드된다.
        self.assertEqual(response.status_code, 200) #서버에서 요청한 페이지를 찾을 수 없을경우에 404 Error를 돌려주고 그렇지 않고 정상적으로 페이지를 돌려줄 시에는 status_code로 200을 보내도록 약속함

        #1.3 페이지 타이틀은 'Blog 이다.'
        soup = BeautifulSoup(response.content, 'html.parser') #HTML을 읽어 오기 위해 BeautifulSoup함수를 이용하여  html 을 읽어오고 html.parser명령어로 파싱한 결과를 soup 함수 안에 넣는다.
        self.assertEqual(soup.title.text, 'Blog')              #그리고 페이지의 title Text만 가져와 그 텍스타가 Blog인지 확인 합니다.

        #1.4 내비게이션 바가 있다.
        navbar = soup.nav #soup.nav의 명령어로 soup의 네비게이션(nav)만 가져와 navbar에 담습니다.

        #1.5 Blog, About Me 라는 문구가 내비게이션 바에 있다.
        self.assertIn('Blog', navbar.text)       #위에 담았던 nav 바에서 텍스트가 blog인지 확인 한다.
        self.assertIn('About Me', navbar.text)   #위에 담았던 nav 바에서 텍스트가 About Me인지 확인 한다.

        #2.1 포스트(게시물)가 하나도 없다면
        self.assertEqual(Post.objects.count(),0) #Post갯수가 0개인지 확인합니다.(Test시에 가상 DB가 만들어지므로 포스트가 0개야 한다.)

        #2.2 main area에 '아직 게시물이 없습니다.'라는 문구가 나타난다.
        main_area = soup.find('div', id='main-area')            #ic가 "main-area"인  div 를 main_area에 넣는다
        self.assertIn('아직 게시물이 없습니다.', main_area.text)    #원래는 DB에 저장되여 있는 Post가 없어야 정상임 그러므로 main_area.text를 호출하여 아직 게시물이 없습니다. 가 호출되는지 확인함

        #3.1 포스트가 2개 있다면
        post_001 = Post.objects.create(
            title = '첫 번째 포스트 입니다.',
            content = 'Hello World. We are the world.',
        )
        post_002 = Post.object.create(
            title = '두 번째 포스트 입니다.',
            content = '두번째가 전부는 아니잖아요?',
        )
        self.assertEqual(Post.objects.count(),2)

        #3.2 포스트 목록 페이지를 새로고침 했을 때
        response = self.clinet.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)

        #3.3 main area에 포스트 2개의 제목이 존재한다.
        main_area = soup.find('div', id='main-area')
        self.assertIn(post_001.title, main_area.text)
        self.assertIn(post_002.title, main_area.text)

        #3.4 '아직 게시물이 없습니다. 라는 문구는 더이상 나타나지 않습니다.'
        self.assertNotIn('아직 게시물이 없습니다.', main_area.text)

    def test_post_detail(self):
        # 1.1 포스트가 하나 있다.
        post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. We are the world.',
        )

        # 1.2 그 포스트의 url은 '/blog/1/'이다.
        self.assertEqual(post_001.get_absolute_url(),'/blog/1/')

        # 2. 첫 번째 포스트의 상세 페이지 테스트
        # 2.1 첫 번째 목록 포스트의 url 로 접근하면 정상적으로 작동한다.
        response = self.client.get(post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        # 2.2 포스트 목록 페이지와 똑같은 내비게이션 바가 있다.
        navbar = soup.nav
        self.assertIn('Blog', navbar.text)
        self.assertIn('About Me', navbar.text)

        # 2.3 첫 번째 포스트의 제목이 웹 브라우저 탭 타이틀에 들어있다.
        self.assertIn(post_001.title,soup.title.text)

        # 2.4 첫 번째 포스트의 제목이 포스트 영역(post_area)에 있다.
        main_area = soup.find('div', id = 'main_area')
        post_area = main_area.find('div', id = 'post_area')
        self.assertIn(post_001.title, post_area.text)

        # 2.5 첫 번째 포스트의 작성자(author)가 포스트 영역에 있다(아직 구현할 수 없음)


        # 2.6 첫 번째 포스트의 내용(content)이 포스트 영역에 있다.
        self.assertIn(post_001.content ,post_area.text)
# Create your tests here.
