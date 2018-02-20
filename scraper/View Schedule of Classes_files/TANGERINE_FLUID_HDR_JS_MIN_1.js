
(function(){


var searchLink = document.querySelector('#pthdrSrchHref');var actionlistSearch = document.querySelector('#pthdr2actionlistsearch');if(searchLink && actionlistSearch)
{
 var searchUrl = searchLink.getAttribute("searchurl"); actionlistSearch.setAttribute("onclick","DoSearch('BASIC','"+searchUrl+"')"); actionlistSearch.setAttribute("href","#");}
else
{
 ptUtil.addClass(actionlistSearch, 'hideActionMenuSearchLink');}


var headerIconsList = document.querySelectorAll("#pthdr2navbarlinks a");for (var index = 0; index < headerIconsList.length; index++)
{
 var currentElement = headerIconsList[index]; var style = window.getComputedStyle(currentElement); if(style.display === 'block' || style.display === 'inline' )
 { 
 var onKeyDownAttr = currentElement.getAttribute("onkeydown"); if(!onKeyDownAttr)
 {
 currentElement.setAttribute("onkeydown","registerHeaderKeyPress(event)"); }
 }
}


var actionListLinks = document.querySelectorAll("#ACTION_LINK_CONTAINER a.PSHYPERLINK");for (var index = 0; index < actionListLinks.length; index++)
{
 var currentElement = actionListLinks[index]; var roleAttr = currentElement.getAttribute("role"); if(!roleAttr)
 {
 var currentElementRole = currentElement.getElementsByTagName("span")[0] ; if(currentElementRole)
 currentElementRole.setAttribute("role","listitem"); else
 currentElement.setAttribute("role","listitem"); }
}

}());function registerHeaderKeyPress(event) {
 var currentTarget = event.currentTarget || event.srcElement; if(isActionListShown())
 {
 switch (event.keyCode)
 {
 case 27: hideActionListMenu();  break; case 9 : if(findLastLinkOfActionList(currentTarget)) { 
 event.preventDefault();  loopBackFocusIntoActionList(); } 
 break;  case 38: event.preventDefault();  break; case 40: event.preventDefault();  break; }
 }
 else
 {
 switch (event.keyCode)
 {
 case 32: event.preventDefault();  currentTarget.onclick();  break; }
 }

 return true;}


function isActionListShown() {
 var actionListContainerClass = document.getElementById("pthdr2actionListcontainerfluid").className ; if(actionListContainerClass.indexOf("showActionListMenu") >= 0)
 return true ; else
 return false ;}


function findLastLinkOfActionList(obj) {

 var actionListLinks = new Array(); var lastElementOfActionlist = ""; var actionmenu = document.getElementById("ACTION_LINK_CONTAINER"); if(actionmenu) 
 var nodeList = actionmenu.querySelectorAll("a.ps-link, a.PSHYPERLINK"); for (var index = 0; index < nodeList.length; index++)
 {
 var currentActionListItem = nodeList[index]; var style = window.getComputedStyle(currentActionListItem); if(style.display === 'block')
 {
 actionListLinks.push(currentActionListItem); }
 }

 if(actionListLinks.length > 0)
 lastElementOfActionlist = actionListLinks[actionListLinks.length-1].id; if(obj.id && lastElementOfActionlist && (obj.id == lastElementOfActionlist))
 return true; else
 return false;}


function focusIntoActionList() {
 var actionListTitle = document.getElementById('actionListTitle'); var actionlistheader = document.getElementById('actionListHeader'); var style = window.getComputedStyle(actionlistheader); if(actionListTitle && style.display === 'block')
 actionListTitle.focus(); else
 focusFirstLinkOfActionList(); return true;}


function loopBackFocusIntoActionList() {
 var actionlistCloseIcon = document.getElementById('closeAnchor'); var actionlistheader = document.getElementById('actionListHeader'); var style = window.getComputedStyle(actionlistheader); if(actionlistCloseIcon && style.display === 'block')
 closeAnchor.focus(); else
 focusFirstLinkOfActionList(); return true;}


function focusFirstLinkOfActionList() {
 var actionmenu = document.getElementById("ACTION_LINK_CONTAINER"); if(actionmenu) 
 var nodeList = actionmenu.querySelectorAll("a.ps-link, a.PSHYPERLINK"); for (var index = 0; index < nodeList.length; index++)
 {
 var currentActionListItem = nodeList[index]; var style = window.getComputedStyle(currentActionListItem); if(style.display === 'block') { 
 nodeList[index].focus();  break;  }
 }
 return true;}


function closeActionList(event) {
 var currentTarget = event.currentTarget || event.srcElement; switch (event.keyCode)
  {
 case 27: hideActionListMenu();  break; case 32: event.preventDefault();  hideActionListMenu();  break; case 13: event.preventDefault();  hideActionListMenu();  break; }
 return true;}


function registerSearchTrayKeyPress(event) {
 var currentTarget = event.currentTarget || event.srcElement; switch (event.keyCode)
  {
 case 27: hideSearchContainer();  document.getElementById('pthdr2Search').focus();  break; }
 return true;}