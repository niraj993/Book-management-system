from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib import messages

@login_required(login_url="login_user")
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


 
@login_required(login_url="login_user")   
def book_update(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    
    if not book:
        messages.error(request, "Book not found.")
        return redirect('book_list')   
    
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        image = request.FILES.get('image')
       
        book.title = title
        book.author = author
        book.description = description
        if image:
            book.image = image
        
        book.save()
        messages.success(request, "Book updated successfully.")   
        return redirect('book_list')   

    return render(request, 'books/book_edit.html', {'book': book})


@login_required(login_url="login_user")
def book_delete(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    if not book:
        print("asdfghjk")
        print(book)
    

    if request.method == 'POST':
        book.delete()   
        return redirect('book_list')   
    
    return render(request, 'books/book_delete.html', {'book': book})

        



# def book_create(request):
#     if request.method == 'POST':

#     return render(request, 'books/book_form.html', {'form': form})

# def book_update(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'books/book_form.html', {'form': form})

# def book_delete(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book_list')
#     return render(request, 'books/book_confirm_delete.html', {'book': book})

