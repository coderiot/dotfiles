# use inkscape for missing pdf_tex files
add_cus_dep('svg', 'pdf_tex', 0, 'svg2pdf');
sub svg2pdf {
    system("inkscape -D -z --file=\"$_[0].svg\" --export-pdf=\"$_[0].pdf\" --export-latex");
}
