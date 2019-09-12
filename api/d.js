  var single_video_form = $('#single_video_question_form');
      var multiple_videos_form = $("#multiple_videos_question_form");

      single_video_form.submit(function (e) {

        e.preventDefault();
          const url = $("#downloadVideoUrl").attr("data-url");

          notify("download request started ...", true)

        $.ajax({
            type: 'POST',
            url: url,
            data: single_video_form.serialize(),
            success: function (data) {
              notify(data.answer, true)
            },
            error: function (data) {
                notify('An error occurred :' + data.message, false);
                console.log('An error occurred :' + data.message)
                console.log(data)
            },
        });
      })

      multiple_videos_form.submit(function (e){
        e.preventDefault();
        var url = $("#downloadVideoList").attr("data-url");
        notify("download list request started ...", true)


        $.ajax({
            type: 'POST',
            url: url,
            data: multiple_videos_form.serialize(),
            success: function (data) {
              notify(data.answer, true)
            },
            error: function (data) {
                notify('An error occurred :' + data.message, false);
                console.log('An error occurred :' + data.message)
                console.log(data)
            },
        });
      })


