$(document).ready(function() {

	$(function listTools() {

		$.getJSON("https://spreadsheets.google.com/feeds/list/1hCqYbVg_h6B4YqsNOXXh0tFKwbcUJ8tVeGXryZimOG8/1/public/values?alt=json-in-script&callback=?", 
			function(data) {
				$('div#tools_list').append('<ul class="items"></ul>');
					$.each(data.feed.entry, function(i, entry) {
						var item = entry.gsx$tool.$t;
							$('.items').append('<li>' + item + '</span></li>');

					});
				});
	});
});
