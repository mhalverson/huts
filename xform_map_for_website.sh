#!/bin/bash

raw_map=$1; shift
js_file=$1; shift

# find the suitable place to insert a <script> line: before the first <link>
insert_script_line=$(grep -n '\<link ' "$raw_map" | head -n 1 | cut -d : -f 1)

# find the identifier for the map: the first style describing the map proportions
map_identifier=$(egrep '\<style>#map_[a-zA-Z0-9]+ \{' "$raw_map" | egrep -o 'map_[a-zA-Z0-9]+')

# alter the width and left
map_style_start_line=$(egrep -n '\<style>#map_[a-zA-Z0-9]+ \{' "$raw_map" | head -n 1 | cut -d : -f 1)
# assume the next two lines are 'position' and 'width'
map_style_end_offset=$(tail -n +$map_style_start_line "$raw_map" | grep -n '</style>' | head -n 1 | cut -d : -f 1)
map_style_end_line=$(($map_style_start_line + $map_style_end_offset - 1))

map_div_line=$(grep -n '<div class="folium-map".*></div>' "$raw_map" | head -n 1 | cut -d : -f 1)
last_line=$(wc -l "$raw_map" | awk '{print $1}')

# put it all together
cat "$raw_map" | head -n $(($insert_script_line - 1))
echo "    <script src=\"$js_file\"></script>"
echo '    <!-- Global site tag (gtag.js) - Google Analytics -->'
echo '    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-139615802-1"></script>'
echo '    <script>'
echo '      window.dataLayer = window.dataLayer || [];'
echo '      function gtag(){dataLayer.push(arguments);}'
echo "      gtag('js', new Date());"
echo "      gtag('config', 'UA-139615802-1');"
echo '    </script>'
echo "    <title>Hut map</title>"
cat "$raw_map" | tail -n +$(($insert_script_line)) | head -n $(($map_style_start_line - $insert_script_line + 1))
echo '        position: fixed;'
echo '        width: 70.0%;'
cat "$raw_map" | tail -n +$(($map_style_start_line + 3)) | head -n $(($map_style_end_offset - 3))
echo '    <link rel="stylesheet" href="/assets/css/styles.css">'
echo '    <style>body{max-width: unset; margin-left: unset;}</style>'
echo '    <style>#summaryzone{margin-left: 70%; padding-left: 5px;}</style>'
cat "$raw_map" | tail -n +$(($map_style_end_line + 1)) | head -n $(($map_div_line - $map_style_end_line - 1))
echo "    <div class=\"folium-map\" id=\"${map_identifier}\"></div>"
echo '    <div id="summaryzone"></div>'
cat "$raw_map" | tail -n +$(($map_div_line + 1)) | head -n $(($last_line - $map_div_line - 1))
cat <<'EOF'
	$('#summaryzone').html('<p>Initially, the map shows all the huts I\'ve visited. You can click on the markers to show information about each hut.</p><p>If you click on the "layers" icon in the upper-right corner, you will see two layers for each region: one for huts I have visited, and one for huts I haven\'t visited. You can enable or disable each layer separately. When you enable a layer, the checklist for that region will be shown on the right.</p><p>If you like, you can change the map to "terrain mode" by going to layers and selecting the "stamenterrain" tileset.</p><p>To see these instructions again, simply refresh the page.</p>');
EOF
echo "$map_identifier.on('overlayadd', function(overlay) {"
cat <<'EOF'
	$('#summaryzone').html(checklist_data[overlay.name.split(' - ')[0]]);
	return true;
});
</script>
EOF
