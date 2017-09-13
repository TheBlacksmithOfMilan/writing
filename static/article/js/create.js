$(function(){

    editor = editormd("editormd", {
        lineNumbers: true,
        height  : 600,
        tex  : true,
        syncScrolling : "single",
        // codeFold: true,
        path    : "/static/libs/editor-md/lib/",
        toolbarIcons : function() {
            // Or return editormd.toolbarModes[name]; // full, simple, mini
            return editormd.toolbarModes['simple'];
            // return ["undo", "redo", "|", "bold", "hr"]
        },
    });


    $('.btn-article-save').on('click', function(event) {
        event.preventDefault();
        var $form = $($(this).data('target'))
        var status = $(this).data('status')

        var msg = ''
        if (status=='publisher') {
            msg = '发布后不可编辑，确定要发布吗？'
        } else {
            msg = '确定要保存吗？'
        }

        layer.confirm(msg, {
          btn: ['确定','取消'] //按钮
        }, function(){
            $.ajax({
                url: $form.attr('action'),
                type: 'POST',
                dataType: 'json',
                data: $form.serialize() + "&status=" + status,
            })
            .done(function(response) {
                if (response.status=='success') {
                    layer.msg('successfully');
                    setTimeout(function(){
                        if (response.url) window.location.href = response.url
                    }, 500);
                } else {
                    layer.msg('sorry.');
                }
            })
            .fail(function() {
                layer.msg('sorry.');
            })

        }, function(){
        });

    });


})