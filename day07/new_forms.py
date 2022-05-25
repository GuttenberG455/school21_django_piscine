class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'synopsis', 'content')

