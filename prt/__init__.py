"""
for each pixel do
  compute viewing ray
  if ray hits an object with t in [0,inf) then
    compute normal vector n
    evaluate shading model and set pixel to the resulting color
  else
    set pixel to the background color
"""
