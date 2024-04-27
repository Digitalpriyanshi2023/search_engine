from django.shortcuts import render
from django.db.models import Q
from .models import SearchResult

def search_view(request):
    query = request.GET.get('q')
    results = []

    # Debugging print statement
    print(f"Query received: {query}")

    if query:
        # Search logic
        results = SearchResult.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        # Debugging print statement
        print(f"Results found: {len(results)}")

    # Return the results to the template
    return render(request, 'search/search.html', {'query': query, 'results': results})
