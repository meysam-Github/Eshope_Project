function sendArticleComment(){
    // console.log('submit article comment');
    var comment = $('#commentText').val();
    
    $.get('/articles/add-article-comment', {
        articleComment : comment,
        articleId : 32,
        parentId : null,

    }).then(res => {
        console.log(res)
    });
}