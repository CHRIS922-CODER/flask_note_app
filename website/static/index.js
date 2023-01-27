function deleteNote(noteId){
    fetch('/delete-note',
    {
        method:'POST',
        body: JSON.stringify({noteId: noteId})

    }).then((_res)=>{
        // reloading the window and redirecting us to the home page
        window.location.href="/";
    })

}