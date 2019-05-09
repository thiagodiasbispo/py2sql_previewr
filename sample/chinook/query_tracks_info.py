from pypika.queries import Query, make_tables

tracks, playlists, playlist_track = make_tables("tracks", "playlists", "playlist_track")

query = (
    Query.from_(playlist_track)
    .join(playlists)
    .using("playlistid")
    .join(tracks)
    .using("trackid")
    .select(
        playlists.name.as_("Playlist name"),
        tracks.name.as_("track_name"),
        tracks.composer,
        tracks.milliseconds,
    )
    .orderby(playlists.name, tracks.name)
)
