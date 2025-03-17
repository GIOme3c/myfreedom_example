from book.models import Book

def test_context(request):
    ud = request.COOKIES.get("sessionid", None)
    return {"user_data": Book.objects.get(id=1)}