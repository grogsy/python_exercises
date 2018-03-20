set nocompatible		"be iMproved, required
filetype off			"required
set encoding=utf-8
set nu
set guifont=Consolas:h10 
colorscheme slate

"set the runtime path to include Vundle and initialize
set rtp+=$HOME/.vim/bundle/Vundle.vim/
call vundle#begin('$HOME/.vim/bundle/')

"let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

set splitbelow
set splitright

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

"enable folding
set foldmethod=indent
set foldlevel=99

"enable folding with spacebar
nnoremap <space> za

"Add all plugins here
Plugin 'tmhedberg/SimpylFold'
let g:SimplyFold_docstring_preview=1

Plugin 'vim-scripts/indentpython.vim'

Plugin 'vim-syntastic/syntastic'

Plugin 'nvie/vim-flake8'

let python_highlight_all=1
syntax on


Plugin 'scrooloose/nerdtree'
Plugin 'jistr/vim-nerdtree-tabs'

"super searching
"hit ctrl-p to search for things
Plugin 'kien/ctrlp.vim'


"Bundle 'Valloric/YouCompleteMe'
"let g:ycm_autoclose_preview_window_after_completion=1
"map <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>
highlight BadWhiteSpace ctermbg=red guibg=darkred
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

au BufNewFile,BufRead *.py
	\ set tabstop=4
	\ set softtabstop=4
	\ set shiftwidth=4
	\ set textwidth=79
	\ set expandtab
	\ set autoindent
	\ set fileformat=unix

au BufNewFile,BufRead *.js,*.html,*.css
	\ set tabstop=2
	\ set softtabstop=2
	\ set shiftwidth=2




"All plugins must be added before the following line
call vundle#end()		"required
filetype plugin indent on	"required

"python with virtualenv support
"py << EOF
"import os
"import sys
"if 'VIRTUAL_ENV' in os.environ:
"	project_base_dir = os.environ['VIRTUAL_ENV']
"	activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
"	execfile(activate_this, dict(__file__=activate_this))
"EOF

	
