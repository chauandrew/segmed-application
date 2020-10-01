$(document).ready(function() {
    $('.card').find('button').on('click', function(ev) {
        let cardId = ev.target.parentNode.parentNode.id

        // toggle border / photo flag
        if ($(ev.target).text().includes('unflag')) {
            $(ev.target).text('flag photo')
            $(`#${cardId}`).removeClass('border border-dark')
        } else {
            $(ev.target).text('unflag photo')
            $(`#${cardId}`).addClass('border border-dark')
        }
        // get pictureId and make backend call to toggle flag
        pictureId = cardId.substr(10)
        pictureId = parseInt(pictureId)
        $.ajax({
            type:"POST",
            url: `/api/v1/flag?id=${pictureId}`
        })
    })
})