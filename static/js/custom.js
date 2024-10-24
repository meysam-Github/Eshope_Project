function sendArticleComment(articleId){
    // console.log('submit article comment');
    var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
    

    $.get('/articles/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId,

    }).then(res => {
        $('#comments_area').html(res);
        $('#commentText').val(' ');
        $('#parent_id').val(' ');
        

        if(parentId !== null && parentId !== ''){
            document.getElementById('single_comment_box_' + parentId ).scrollIntoView( {behavior: "smooth"} );

        } else{
            document.getElementById('comment_area').scrollIntoView( {behavior: "smooth"} );

        }
        
    })
}

function fillParnetId(parentId){
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView( {behavior: "smooth"} );
}