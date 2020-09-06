import React, { Component } from "react";

class MovieListComp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("movies/api")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    return (
        <div>
        <h3>Movies</h3>
        <table class="table table-striped">
        <thead>
            <tr>
            <th>Title</th>
            <th>Year</th>
            <th>Genre</th>
            <th colspan="2">Action</th>
            </tr>
        </thead>
        <tbody>
            {this.state.data.map(movie => {
                return (
                    <tr>
                    <td>{movie.title}</td>
                    <td>{movie.year}</td>
                    <td>{movie.genre}</td>
                    <td><a class="btn btn-sm btn-info" href="">Edit</a></td>
                    <td><a class="btn btn-sm btn-danger" href="">Delete</a></td>
                  </tr>
            );
            })}
        </tbody>
    </table>
    </div>
    );
  }
}

export default MovieListComp;