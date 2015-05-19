class CreateTracks < ActiveRecord::Migration
  def change
    create_table :tracks do |t|
	  t.string :name
	  t.string :minutes
	  t.string :album_id
	  t.references :model

      t.timestamps null: false
    end
  end
end
