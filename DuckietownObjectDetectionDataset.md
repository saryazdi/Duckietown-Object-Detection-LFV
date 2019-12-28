<h1>The Duckietown Object Detection Dataset</h1>
This dataset can be found <a href="https://drive.google.com/drive/folders/1cTBoKrXJb0kajBGxhuBxJpbKaotHPX7O">here</a>. We provide annotations and a sample script to load the annotations.


<table>
      <tr><td>Number of images</td><td>1956</td></tr>
      <tr><td>Number of object categories</td><td>3</td></tr>
      <tr><td>Number of objects annotated</td><td>5068</td></tr>
</table>

<h2>Category Details</h2>
<h3>Duckies</h3>
<table>
      <tr><td>Category name</td><td>duckie</td></tr>
      <tr><td>Number of instances</td><td>2570</td></tr>
      <tr><td>Category id</td><td>2</td></tr>
</table>


<h3>Cones</h3>
<table>
      <tr><td>Category name</td><td>cone</td></tr>
      <tr><td>Number of instances</td><td>372</td></tr>
      <tr><td>Category id</td><td>1</td></tr>
</table>


<h3>Duckiebots</h3>
<table>
      <tr><td>Category name</td><td>duckiebot</td></tr>
      <tr><td>Number of instances</td><td>2126</td></tr>
      <tr><td>Category id</td><td>3</td></tr>
      <tr><td>Number of older Duckiebot instances</td><td>1419</td></tr>
      <tr><td>Number of newer Duckiebot instances</td><td>707</td></tr>
</table>


In this work, we first identify most prominent objects. In the duckietown, we see duckies, duckiebots and cones on the road. To achieve this, we find useful logs containing all these obstacles. We preprocess these logs to get diverse set of frames with multiple obstacles. 

