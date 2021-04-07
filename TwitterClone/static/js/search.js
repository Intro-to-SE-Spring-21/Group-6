$( function() {
    $("#search").autocomplete( {
        source: "/ajax_calls/search/",
        minLength: 2,
        select: function( event, ui ) { 
            window.location.href = ui.item.url;
        }
    });
});