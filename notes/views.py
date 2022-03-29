from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        nomeTag = request.POST.get('tag')
        nomeTag = nomeTag.lower()
        if len(nomeTag)==0:
            nomeTag=""
        tag, created = Tag.objects.get_or_create(title=nomeTag)
        if created:
            tag.save()        
        note = Note(title = title, content=content,tag=tag)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        tags = Tag.objects.exclude(title="").all()
        
        #Eliminando tags não utilizadas
        tags_in_notes = list(set([k.tag.title for k in list(all_notes)]))
        total_tags = [g.title for g in list(tags)]
        tags_empty = [x for x in total_tags if x not in tags_in_notes]
        if len(tags_empty)!=0:
            for tag in tags_empty:
                tag1 = Tag.objects.get(title=tag)
                tag1.delete()
                return redirect('index')

        return render(request, 'notes/index.html', {'notes': all_notes,'tags':tags})

def getByTag(request):
    nomeTag = request.POST.get('tag')
    if nomeTag=="todos":
        return redirect('index')

    notes = Note.objects.filter(tag=nomeTag)
    tag=Tag.objects.exclude(title="").all()
    return render(request, 'notes/tagfilter.html', {'tags':tag,'notes': notes})
    
def tags(request):
    tags = Tag.objects.exclude(title="").all()
    return render(request, 'notes/tags.html', {'tags':tags})

def delete(request):
    id = request.POST.get('id').split("/")[0]
    b = Note.objects.get(pk=int(id))
    b.delete()
    return redirect('index')

def tags(request):
    tags = Tag.objects.exclude(title="").all()
    return render(request, 'notes/tags.html', {'tags':tags})


def update(request):
    title = request.POST.get('title')
    content = request.POST.get('details')
    id = request.POST.get('id').split("/")[0]
    tags = request.POST.get('tags')
    tag, created = Tag.objects.get_or_create(title=tags)
    if created:
        tag.save()        
    Note.objects.filter(id=id).update(title=title,content=content,tag=tag)
    return redirect('index')
