
$().ready(function(){
    function createMovieCard(id, movie){
        let people_dom = "<p>People Not Found</p>"
        if (movie.people){
            people_dom = "<ul class='people-list'>";
            for(var people of movie.people){
                people_dom += `<li>${people}</li>`
            }
            people_dom += "</ul>";
        }
        const dom = `
            <div class="card">
                <div class="card-header" id="heading-${id}">
                    <h2 class="mb-0">
                        <button 
                            class="btn btn-link collapsed"
                            type="button"
                            data-toggle="collapse"
                            data-target="#collapse-${id}"
                            aria-expanded="false"
                            aria-controls="collapse-${id}"
                        >
                        ${movie.title} - ${movie.release_date}
                        </button>
                    </h2>
                </div>
                <div
                    id="collapse-${id}"
                    class="collapse"
                    aria-labelledby="heading-${id}"
                    data-parent="#movies_body"
                >
                    <div class="card-body">
                        ${people_dom}
                    </div>
                </div>
            </div>
        `
        return dom;
    }
    function createMoviesBody(movies){
        let dom = `
            <div class="card">
                <div class="card-header">
                    Movies Not Found
                </div>
            </div>
        `
        if (movies){
            dom = `
                <div class="accordion" id="movies_body">
            `
            Object.values(movies).forEach(
                (movie, index) => { dom += createMovieCard(index, movie); }
            );
            dom += "</div>";
        }
        return dom;
    }
    const wsScheme = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
    const wsPath = wsScheme + window.location.host + window.location.pathname + "/stream";
    const socket = io(wsPath);
    socket.on('update_movies', function(data){
        const movies = data.movies;
        const fetchedAt = data.fetched_at;
        $('#fetched_at').text("Fetched At: " + fetchedAt);
        $('#movies').empty();
        $('#movies').html(createMoviesBody(movies));
    })
});