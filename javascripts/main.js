$(function() {
    var reposEl = $('#repos')
        ,repos = ['quark', 'Neutrino', 'one', 'x-bootstrap']
        ,template = _.template($('#repo-template').html())

    $.each(repos, function() {
        $.ajax('https://api.github.com/repos/lytc/' + this, {
            dataType: 'jsonp'
            ,success: function(result) {
                reposEl.append(template(result.data))
            }
        })
    })
})